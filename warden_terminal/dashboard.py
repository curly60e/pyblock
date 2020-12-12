import urwid
import subprocess
from datetime import datetime
from ansi_management import (warning, success, error, info, clear_screen, bold)
from data import data_tor, data_btc_price, data_login, data_mempool
from dependencies.urwidhelper.urwidhelper import translate_text_for_urwid


def main_dashboard(config, tor, spinner):

    try:
        refresh_interval = int(config['MAIN'].get('refresh'))
    except Exception:
        refresh_interval = 5

    running_jobs = {
        'btc': {
            'workers': 0,
            'pipe': None
        },
        'tor': {
            'workers': 0,
            'pipe': None
        },
        'login': {
            'workers': 0,
            'pipe': None
        },
        'mp': {
            'workers': 0,
            'pipe': None
        }
    }

    palette = [('titlebar', 'dark green', ''),
               ('refresh button', 'dark green,bold', ''),
               ('quit button', 'dark green', ''),
               ('getting quote', 'dark blue', ''),
               ('headers', 'white,bold', ''), ('change ', 'dark green', ''),
               ('change negative', 'dark red', '')]

    def exit_on_q(key):
        if key in ('q', 'Q'):
            raise urwid.ExitMainLoop()

    def update_header(layout, message=None, message_type=None):
        # Create Header
        refresh_time = datetime.now().strftime('%H:%M:%S')
        txt = u' WARden Node Version          Last Update on: ' + refresh_time
        if message:
            txt += '    ' + warning(str(message))
        header_text = urwid.Text(txt)
        header = urwid.AttrMap(header_text, 'titlebar')
        layout.header = header

    # Draw empty dashboard
    spinner.stop()
    menu = urwid.Text([u'Press (', ('quit button', u'Q'), u') to quit.'])

    # Create the BTC price box
    quote_text = urwid.Text('Loading Prices...')
    quote_filler = urwid.Filler(quote_text, valign='top', top=1, bottom=1)
    v_padding = urwid.Padding(quote_filler, left=1, right=1)
    quote_box = urwid.LineBox(v_padding)

    # Create the TOR Box
    tor_text = urwid.Text('Checking Tor Status...')
    tor_filler = urwid.Filler(tor_text, valign='top', top=1, bottom=1)
    tor_padding = urwid.Padding(tor_filler, left=1, right=1)
    tor_box = urwid.LineBox(tor_padding)

    # Create user login Box
    login_text = urwid.Text('Loading User Logins...')
    login_filler = urwid.Filler(login_text, valign='top', top=1, bottom=1)
    login_padding = urwid.Padding(login_filler, left=1, right=1)
    login_box = urwid.LineBox(login_padding)

    # Create TMP Box
    mp_text = urwid.Text('Loading Mempool...')
    mp_filler = urwid.Filler(mp_text, valign='top', top=1, bottom=1)
    mp_padding = urwid.Padding(mp_filler, left=1, right=1)
    mp_box = urwid.LineBox(mp_padding)

    # Assemble the widgets
    header = 'Loading...'
    log_tor = urwid.Columns([mp_box, urwid.Pile([login_box, tor_box])])
    body_widget = urwid.Pile([quote_box, log_tor])

    layout = urwid.Frame(header=header, body=body_widget, footer=menu)
    update_header(layout)

    # Handle key presses
    def handle_input(key):
        if key == 'R' or key == 'r':
            refresh(main_loop, '')

        if key == 'Q' or key == 'q':
            raise urwid.ExitMainLoop()

    def refresh(_loop, _data):
        # Add Background Tasks
        update_header(layout)
        main_loop.draw_screen()

        # Add Background Updates
        max_workers = 1  # Max number of threads **KEEP AT 1***
        # Beware of increasing the max_workers - need to make sure
        # processes are killed for all workers - CODE IS NOT DOING THAT
        # right now and will lead to CPU usage blowing up
        if running_jobs['btc']['workers'] < max_workers:
            running_jobs['btc']['workers'] += 1
            stdout = main_loop.watch_pipe(update_btc)
            stderr = main_loop.watch_pipe(update_btc)
            running_jobs['btc']['pipe'] = subprocess.Popen(
                'python3 data.py data_btc_price',
                shell=True,
                stdout=stdout,
                stderr=stderr)

        if running_jobs['tor']['workers'] < max_workers:
            running_jobs['tor']['workers'] += 1
            tor_stdout = main_loop.watch_pipe(update_tor)
            tor_stderr = main_loop.watch_pipe(update_tor)
            running_jobs['tor']['pipe'] = subprocess.Popen(
                'python3 data.py data_tor',
                shell=True,
                stdout=tor_stdout,
                stderr=tor_stderr)

        if running_jobs['login']['workers'] < max_workers:
            running_jobs['login']['workers'] += 1
            tor_stdout = main_loop.watch_pipe(update_login)
            tor_stderr = main_loop.watch_pipe(update_login)
            running_jobs['login']['pipe'] = subprocess.Popen(
                'python3 data.py data_login',
                shell=True,
                stdout=tor_stdout,
                stderr=tor_stderr)

        if running_jobs['mp']['workers'] < max_workers:
            running_jobs['mp']['workers'] += 1
            tor_stdout = main_loop.watch_pipe(update_mp)
            tor_stderr = main_loop.watch_pipe(update_mp)
            running_jobs['mp']['pipe'] = subprocess.Popen(
                'python3 data.py data_mempool',
                shell=True,
                stdout=tor_stdout,
                stderr=tor_stderr)

        main_loop.set_alarm_in(refresh_interval, refresh)

    def update_btc(read_data):
        read_data = translate_text_for_urwid(read_data)
        quote_box.base_widget.set_text(read_data)
        main_loop.remove_watch_pipe = True
        running_jobs['btc']['workers'] = 0
        running_jobs['btc']['pipe'].kill()

    def update_tor(read_data):
        read_data = translate_text_for_urwid(read_data)
        tor_box.base_widget.set_text(read_data)
        running_jobs['tor']['workers'] = 0
        running_jobs['tor']['pipe'].kill()

    def update_login(read_data):
        read_data = translate_text_for_urwid(read_data)
        login_box.base_widget.set_text(read_data)
        running_jobs['login']['workers'] = 0
        running_jobs['login']['pipe'].kill()

    def update_mp(read_data):
        read_data = translate_text_for_urwid(read_data)
        mp_box.base_widget.set_text(read_data)
        main_loop.remove_watch_pipe = True
        running_jobs['mp']['workers'] = 0
        running_jobs['mp']['pipe'].kill()

    main_loop = urwid.MainLoop(layout, palette, unhandled_input=handle_input)

    main_loop.set_alarm_in(0, refresh)
    try:
        main_loop.run()
    except Exception:  # Catch some timeouts - only once
        update_header(layout, message='   Something went Wrong... Relaunched.')
        main_loop.run()