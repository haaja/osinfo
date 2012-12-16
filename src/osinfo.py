#!/usr/bin/env python
#
#   osinfo.py
#
#   Prints miscellaneous information about linux host.
#
#   Licence: MIT (See LICENCE file or http://opensource.org/licenses/MIT)
#   Author: Janne Haapsaari <haaja@iki.fi>
#

import platform
import getpass
import subprocess
import sys


def get_distro_logo(distro='default'):
    """ Function returns ascii representation for distro logo.

    Keyword arguments:
        distro -- name of the linux distribution
    """

    logo = {
        'ubuntu':       "                                               \n"
                        + "              ..''''''..                     \n"
                        + "          .;::::::::::::::;.                 \n"
                        + "       .;::::::::::::::'.':::;.              \n"
                        + "     .;::::::::;,'..';.   .::::;.            \n"
                        + "    .:::::::,.,.      ....:::::::.           \n"
                        + "   .:::::::.   :;::::,.   .:::::::.          \n"
                        + "   ;::::::   .::::::::::.   ::::::;          \n"
                        + "   :::.  .'  ::::::::::::...,::::::          \n"
                        + "   :::.  .'  ::::::::::::...,::::::          \n"
                        + "   ;::::::   .::::::::::.   ::::::;          \n"
                        + "   .:::::::.   :,;::;,.   .:::::::.          \n"
                        + "    .:::::::;.;.      ....:::::::.           \n"
                        + "      ;::::::::;,'..';.   .::::;             \n"
                        + "       .;::::::::::::::'.':::;.              \n"
                        + "          .,::::::::::::::,.                 \n"
                        + "              ...''''...                     \n"
                        + "                                             \n",
        'fedora':       '                                               \n'
                        + '                  ___                        \n'
                        + '            ,g@@@@@@@@@@@p,                  \n'
                        + '         ,@@@@@@@@@@@D****4@@.               \n'
                        + '       ,@@@@@@@@@@P`        `%@.             \n'
                        + '      y@@@@@@@@@@F   ,g@@p.  !3@k            \n'
                        + '     !@@@@@@@@@@@.  !@@@@@@@@@@@@k           \n'
                        + '    :@@@@@@@@@@@@   J@@@@@@@@@@@@@L          \n'
                        + '    J@@@@@@@@@***   `***@@@@@@@@@@)          \n'
                        + '    J@@@@@@@@@          @@@@@@@@@@)          \n'
                        + '    J@@@@@@@@@@@@   J@@@@@@@@@@@@@L          \n'
                        + '    J@@@@@@@@@@@@   J@@@@@@@@@@@@F           \n'
                        + '    J@@@@@@@@@@@F   {@@@@@@@@@@@F            \n'
                        + '    J@@@E.  ``*^`   i@@@@@@@@@@B^            \n'
                        + '    J@@@@@._      ,@@@@@@@@@@P`              \n'
                        + '    J@@@@@@@@@@@@@@@@@@BP*`                  \n'
                        + '                                             \n',
        'mint':         '                                               \n'
                        + '.:::::::::::::::::::::::::;,.                \n'
                        + ',0000000000000000000000000000Oxl,            \n'
                        + ',00,                       ..,cx0Oo.         \n'
                        + ',00,       ,,.                  .cO0o        \n'
                        + ',00l,,.   `00;       ..     ..    .k0x       \n'
                        + '`kkkkO0l  `00;    ck000Odlk000Oo.  .00c      \n'
                        + '     d0k  `00;   x0O:.`d00O;.,k00.  x0x      \n'
                        + '     d0k  `00;  .00x   ,00o   ;00c  d0k      \n'
                        + '     d0k  `00;  .00d   ,00o   ,00c  d0k      \n'
                        + '     d0k  `00;  .00d   ,00o   ,00c  d0k      \n'
                        + '     d0k  `00;   ;;`   .;;.   .cc`  d0k      \n'
                        + '     d0O  .00d                ...   d0k      \n'
                        + '     ;00,  :00x:,,,,        .....   d0k      \n'
                        + '      o0O,  .:dO000k...........     d0k      \n'
                        + '       :O0x,                        x0k      \n'
                        + '         :k0Odc,`.................;x00k      \n'
                        + '           .;lxO0000000000000000000000k      \n'
                        + '                 ......................      \n'
                        + '                                             \n',
        'debian':       '                                               \n'
                        + '              _,met$$$$$gg.                  \n'
                        + '           ,g$$$$$$$$$$$$$$$P.               \n'
                        + '         ,g$$P$$       $$$Y$$.$.             \n'
                        + '        ,$$P`              `$$$.             \n'
                        + '       ,$$P       ,ggs.     `$$b:            \n'
                        + '       d$$`     ,$P$`   .    $$$             \n'
                        + '       $$P      d$`     ,    $$P             \n'
                        + '       $$:      $$.   -    ,d$$`             \n'
                        + '       $$;      Y$b._   _,d$P`               \n'
                        + '       Y$$.     .`$Y$$$$P$`                  \n'
                        + '       `$$b      $-.__                       \n'
                        + '        `Y$$b                                \n'
                        + '         `Y$$.                               \n'
                        + '           `$$b.                             \n'
                        + '             `Y$$b.                          \n'
                        + '               `$Y$b._                       \n'
                        + '                   `$$$$                     \n'
                        + '                                             \n',
        'arch':         '                                               \n'
                        + '                    +                        \n'
                        + '                    #                        \n'
                        + '                   ###                       \n'
                        + '                  #####                      \n'
                        + '                  ######                     \n'
                        + '                #  ######                    \n'
                        + '               ###   #####                   \n'
                        + '              #############                  \n'
                        + '             ###############                 \n'
                        + '            #################                \n'
                        + '           #######      ######               \n'
                        + '          ######         #######             \n'
                        + '         #######         ###   ##            \n'
                        + '        #########       ######               \n'
                        + '       ######               ######           \n'
                        + '       ####                   ####           \n'
                        + '      ##                         ##          \n'
                        + '     #                             #         \n',
        'crunchbang':   '                   ___       ___      _        \n'
                        + '                /  /      /  /     | |       \n'
                        + '               /  /      /  /      | |       \n'
                        + '              /  /      /  /       | |       \n'
                        + '      _______/  /______/  /______  | |       \n'
                        + '     /______   _______   _______/  | |       \n'
                        + '           /  /      /  /          | |       \n'
                        + '          /  /      /  /           | |       \n'
                        + '         /  /      /  /            | |       \n'
                        + '  ______/  /______/  /______       | |       \n'
                        + ' /_____   _______   _______/       | |       \n'
                        + '      /  /      /  /               |_|       \n'
                        + '     /  /      /  /                 _        \n'
                        + '    /  /      /  /                 | |       \n'
                        + '   /__/      /__/                  |_|       \n',
        'default':      '                                               \n'
                        + '                 .88888888:.                 \n'
                        + '                88888888.88888.              \n'
                        + '              .8888888888888888.             \n'
                        + '              888888888888888888             \n'
                        + '              88| _`88|_  `88888             \n'
                        + '              88 88 88 88  88888             \n'
                        + '              88_88_::_88_:88888             \n'
                        + '              88:::,::,:::::8888             \n'
                        + '              88`:::::::::``8888             \n'
                        + '             .88  `::::`    8:88.            \n'
                        + '            8888            `8:888.          \n'
                        + '          .8888`             `888888.        \n'
                        + '         .8888:..  .::.  ...:`8888888:.      \n'
                        + '        .8888.|     :|     `|::`88:88888     \n'
                        + '       .8888        `         `.888:8888.    \n'
                        + '      888:8         .           888:88888    \n'
                        + '    .888:88        .:           888:88888:   \n'
                        + '    8888888.       ::           88:888888    \n'
                        + '    `.::.888.      ::          .88888888     \n'
                        + '   .::::::.888.    ::         :::`8888`.:.   \n'
                        + '  ::::::::::.888   |         .::::::::::::   \n'
                        + '  ::::::::::::.8    |      .:8::::::::::::.  \n'
                        + ' .::::::::::::::.        .:888:::::::::::::  \n'
                        + ' :::::::::::::::88:.__..:88888:::::::::::`   \n'
                        + '  ``.:::::::::::88888888888.88:::::::::`     \n'
                        + '        ``:::_:` -- `` -`-` ``:_::::``       \n'
                        + '                                             \n'
    }

    if distro in logo:
        return logo[distro]
    else:
        return logo['default']


def get_uptime():
    """ Returns system uptime.

    Uptime is read from /proc/uptime file and converted to human readable
    format.
    """

    try:
        file = open('/proc/uptime', 'r')
        data = file.read().split()
        file.close()
    except IOError:
        return 'Unable to open file: /proc/uptime'

    total_seconds = float(data[0])

    # Helper variables
    MINUTE = 60
    HOUR = MINUTE * 60
    DAY = HOUR * 24

    days = int(total_seconds / DAY)
    hours = int((total_seconds % DAY) / HOUR)
    minutes = int((total_seconds % HOUR) / MINUTE)
    seconds = int(total_seconds % MINUTE)

    # build up the result string
    uptime = ''

    if days > 0:
        uptime += str(days) + ' ' + (days == 1 and 'day, ' or 'days, ')
    if hours > 0:
        uptime += str(hours) + ' ' + (hours == 1 and 'hour, ' or 'hours, ')
    if minutes > 0:
        uptime += str(minutes) + ' ' \
            + (minutes == 1 and 'minute, ' or 'minutes, ')
    if seconds > 0:
        uptime += str(seconds) + ' ' \
            + (seconds == 1 and 'second, ' or 'seconds')

    return uptime


def get_loadavg():
    """Returns load averages

    Load averages are read from /proc/loadavg file.
    """

    try:
        file = open('/proc/loadavg', 'r')
        loads = file.readline().split()
        file.close()
    except IOError:
        return 'Unable to open file: /proc/loadavg'

    return str(loads[0] + ', ' + loads[1] + ', ' + loads[2])


def get_kernel_version():
    """Returns kernel version string."""

    return platform.uname()[2]


def get_hostname():
    """Returns hostname."""

    return platform.node()


def get_distribution_info():
    """Returns distribution info."""

    distro = platform.linux_distribution()
    result = distro[0] + ' ' + distro[1] + ' ' + distro[2]

    return result


def get_distribution_name():
    """Returns distribution name."""

    return platform.linux_distribution()[0].lower()


def get_username():
    """Returns the login name of the user."""
    return getpass.getuser()


def get_resolution():
    """Returns screen resolution using xrandr.

    Currently supports only single monitor setups.
    """

    try:
        output = subprocess.check_output(['xrandr'])
    except:
        return "Unable to execute xrandr: " + str(sys.exc_info())

    output = output.split('\n')
    for line in output:
        if "*" in line:
            line = line.strip()
            line = line.split()[0]
            return line

    return "Unable to get screen resolution using xrandr."


def get_number_of_installed_packages():
    """Returns the number of packages installed via distributions package
    manager

    Note: This is really slow!

    Supports following distributions:
        - Fedora
        - SuSE
        - CentOs
        - RedHat
        - Ubuntu
        - Debian
        - Mint
        - Arch
    """

    distro = get_distribution_name()
    output = ''

    if distro == 'fedora' or 'suse' or 'centos' or 'redhat':
        try:
            output = subprocess.check_output(['rpm', '-qa'])
        except:
            return 'Unable to execute rpm: ' + str(sys.exc_info())
    elif distro == 'debian' or 'ubuntu' or 'mint':
        try:
            output = subprocess.check_output(['dpkg', '-l'])
        except:
            return 'Unable to execute dpkg: ' + str(sys.exc_info())
    elif distro == 'arch':
        try:
            output = subprocess.check_output(['pacman', '-Qqu'])
        except:
            return 'Unable to execute pacman: ' + str(sys.exc_info())
    else:
        return 'Unable to count packages'

    output = output.split('\n')

    for i, line in enumerate(output):
        pass

    return str(i)


def get_desktop_environment():
    desktops = {
        'gnome-session': 'GNOME',
        'ksmserver': 'KDE',
        'xfconfd': 'Xfce',
        'cinnamon': 'Cinnamon',
        'unity': 'Unity'
    }

    win_managers = {
        'awesome': 'Awesome',
        'beryl': 'Beryl',
        'blackbox': 'Blackbox',
        'compiz': 'Compiz',
        'dwm': 'DWM',
        'englightenment': 'Enlightenment',
        'fluxbox': 'Fluxbox',
        'fvwm': 'FVWM',
        'icewm': 'IceWM',
        'kwin': 'KWin',
        'metacity': 'Metacity',
        'musca': 'Musca',
        'openbox': 'Openbox',
        'pekwm': 'PekWM',
        'ratpoison': 'ratpoison',
        'scrotwm': 'ScrotWM',
        'wmaker': 'Window Maker',
        'wmii': 'wmii',
        'xfwm4': 'Xfwm',
        'xmonad': 'xmonad'
    }

    try:
        output = subprocess.check_output(['ps', '-e'])
    except subprocess.CalledProcessError as e:
        return "Received CalledProcessError when executing ps -e: " \
            + e.output
    except:
        return 'Unable to execute ps -e: ' + str(sys.exc_info())

    output = output.split('\n')

    for line in output:
        de_process = line.split()[3:]
        if de_process[0] in desktops:
            desktop_environment = desktops[de_process[0]]
            return desktop_environment

    return "Unable to get desktop environment"


def get_de_version(de):

    command = str(de) + ' --version'
    command = command.split()
    output = 'Unable to find DE version.'

    try:
        output = subprocess.check_output(command)
    except subprocess.CalledProcessError as e:
        # For some strange reason at least gnome-session --version returns 1
        # instead of 0
        output = e.output
        pass
    except:
        return 'Unable to execute ' + str(command) + ': ' + sys.exc_info()

    return str(output.split()[1])


if __name__ == '__main__':
    print(get_distro_logo(get_distribution_name()))
    print("Uptime: " + get_uptime())
    print("Kernel: " + get_kernel_version())
    print("Hostname: " + get_hostname())
    print("Distribution: " + get_distribution_info())
    print("User: " + get_username())
    print("Loadavg: " + get_loadavg())
    print("Resolution: " + get_resolution())
    # print("Installed packages: " + get_number_of_installed_packages())
    print("Desktop: " + get_desktop_environment() + " " + get_de_version('gnome-session'))
