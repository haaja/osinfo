#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
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
import os


def get_distro_logo(distro='default'):
    """ Function returns ascii representation for distro logo.

    Keyword arguments:
        distro -- name of the linux distribution
    """

    logo = {
        'ubuntu':
            "                                                   \n"
            + "           ..''''''..                            \n"
            + "       .;::::::::::::::;.                        \n"
            + "    .;::::::::::::::'.':::;.                     \n"
            + "  .;::::::::;,'..';.   .::::;.                   \n"
            + " .:::::::,.,.      ....:::::::.   {uptime}       \n"
            + ".:::::::.   :;::::,.   .:::::::.  {kernel}       \n"
            + ";::::::   .::::::::::.   ::::::;  {host}         \n"
            + ":::.  .'  ::::::::::::...,::::::  {distro}       \n"
            + ":::.  .'  ::::::::::::...,::::::  {user}         \n"
            + ";::::::   .::::::::::.   ::::::;  {load}         \n"
            + ".:::::::.   :,;::;,.   .:::::::.  {reso}         \n"
            + " .:::::::;.;.      ....:::::::.   {pkgs}         \n"
            + "   ;::::::::;,'..';.   .::::;     {desktop}      \n"
            + "    .;::::::::::::::'.':::;.                     \n"
            + "       .,::::::::::::::,.                        \n"
            + "           ...''''...                            \n"
            + "                                                 \n",

        'fedora':
            '                                                   \n'
            + '              ___                                \n'
            + '        ,g@@@@@@@@@@@p,                          \n'
            + '     ,@@@@@@@@@@@D****4@@.                       \n'
            + '   ,@@@@@@@@@@P`        `%@.      {uptime}       \n'
            + '  y@@@@@@@@@@F   ,g@@p.  !3@k     {kernel}       \n'
            + ' !@@@@@@@@@@@.  !@@@@@@@@@@@@k    {host}         \n'
            + ':@@@@@@@@@@@@   J@@@@@@@@@@@@@L   {distro}       \n'
            + 'J@@@@@@@@@***   `***@@@@@@@@@@)   {user}         \n'
            + 'J@@@@@@@@@          @@@@@@@@@@)   {load}         \n'
            + 'J@@@@@@@@@@@@   J@@@@@@@@@@@@@L   {reso}         \n'
            + 'J@@@@@@@@@@@@   J@@@@@@@@@@@@F    {pkgs}         \n'
            + 'J@@@@@@@@@@@F   {@@@@@@@@@@@F     {desktop}      \n'
            + 'J@@@E.  ``*^`   i@@@@@@@@@@B^                    \n'
            + 'J@@@@@._      ,@@@@@@@@@@P`                      \n'
            + 'J@@@@@@@@@@@@@@@@@@BP*`                          \n'
            + '                                                 \n',

        'mint':
            '                                                      \n'
            + '.:::::::::::::::::::::::::;,.                       \n'
            + ',0000000000000000000000000000Oxl,                   \n'
            + ',00,                       ..,cx0Oo.                \n'
            + ',00,       ,,.                  .cO0o               \n'
            + ',00l,,.   `00;       ..     ..    .k0x              \n'
            + '`kkkkO0l  `00;    ck000Odlk000Oo.  .00c  {uptime}   \n'
            + '     d0k  `00;   x0O:.`d00O;.,k00.  x0x  {kernel}   \n'
            + '     d0k  `00;  .00x   ,00o   ;00c  d0k  {host}     \n'
            + '     d0k  `00;  .00d   ,00o   ,00c  d0k  {distro}   \n'
            + '     d0k  `00;  .00d   ,00o   ,00c  d0k  {user}     \n'
            + '     d0k  `00;   ;;`   .;;.   .cc`  d0k  {load}     \n'
            + '     d0O  .00d                ...   d0k  {reso}     \n'
            + '     ;00,  :00x:,,,,        .....   d0k  {pkgs}     \n'
            + '      o0O,  .:dO000k...........     d0k  {desktop}  \n'
            + '       :O0x,                        x0k             \n'
            + '         :k0Odc,`.................;x00k             \n'
            + '           .;lxO0000000000000000000000k             \n'
            + '                 ......................             \n'
            + '                                                    \n',

        'debian':
            '                                                   \n'
            + '       _,met$$$$$gg.                             \n'
            + '    ,g$$$$$$$$$$$$$$$P.                          \n'
            + '  ,g$$P$$       $$$Y$$.$.                        \n'
            + ' ,$$P`              `$$$.                        \n'
            + ',$$P       ,ggs.     `$$b: {uptime}              \n'
            + 'd$$`     ,$P$`   .    $$$  {kernel}              \n'
            + '$$P      d$`     ,    $$P  {host}                \n'
            + '$$:      $$.   -    ,d$$`  {distro}              \n'
            + '$$;      Y$b._   _,d$P`    {user}                \n'
            + 'Y$$.     .`$Y$$$$P$`       {load}                \n'
            + '`$$b      $-.__            {reso}                \n'
            + ' `Y$$b                     {pkgs}                \n'
            + '  `Y$$.                    {desktop}             \n'
            + '    `$$b.                                        \n'
            + '      `Y$$b.                                     \n'
            + '        `$Y$b._                                  \n'
            + '            `$$$$                                \n'
            + '                                                 \n',
        'arch':     '                                               \n'
            + '               +                                 \n'
            + '               #                                 \n'
            + '              ###                                \n'
            + '             #####                               \n'
            + '             ######                              \n'
            + '           #  ######             {uptime}        \n'
            + '          ###   #####            {kernel}        \n'
            + '         #############           {host}          \n'
            + '        ###############          {distro}        \n'
            + '       #################         {user}          \n'
            + '      #######      ######        {load}          \n'
            + '     ######         #######      {reso}          \n'
            + '    #######         ###   ##     {pkgs}          \n'
            + '   #########       ######        {desktop}       \n'
            + '  ######               ######                    \n'
            + '  ####                   ####                    \n'
            + ' ##                         ##                   \n'
            + '#                             #                  \n',

        'crunchbang':
            '                  ___       ___      _             \n'
            + '               /  /      /  /     | |            \n'
            + '              /  /      /  /      | |            \n'
            + '             /  /      /  /       | | {uptime}   \n'
            + '     _______/  /______/  /______  | | {kernel}   \n'
            + '    /______   _______   _______/  | | {host}     \n'
            + '          /  /      /  /          | | {distro}   \n'
            + '         /  /      /  /           | | {user}     \n'
            + '        /  /      /  /            | | {load}     \n'
            + ' ______/  /______/  /______       | | {reso}     \n'
            + '/_____   _______   _______/       | | {pkgs}     \n'
            + '     /  /      /  /               |_| {desktop}  \n'
            + '    /  /      /  /                 _             \n'
            + '   /  /      /  /                 | |            \n'
            + '  /__/      /__/                  |_|            \n',

        'default':
            '                                                       \n'
            + '                .88888888:.                          \n'
            + '               88888888.88888.                       \n'
            + '             .8888888888888888.                      \n'
            + '             888888888888888888                      \n'
            + '             88| _`88|_  `88888                      \n'
            + '             88 88 88 88  88888                      \n'
            + '             88_88_::_88_:88888                      \n'
            + '             88:::,::,:::::8888                      \n'
            + '             88`:::::::::``8888                      \n'
            + '            .88  `::::`    8:88.                     \n'
            + '           8888            `8:888.                   \n'
            + '         .8888`             `888888.                 \n'
            + '        .8888:..  .::.  ...:`8888888:.               \n'
            + '       .8888.|     :|     `|::`88:88888              \n'
            + '      .8888        `         `.888:8888.   {uptime}  \n'
            + '     888:8         .           888:88888   {kernel}  \n'
            + '   .888:88        .:           888:88888:  {host}    \n'
            + '   8888888.       ::           88:888888   {distro}  \n'
            + '   `.::.888.      ::          .88888888    {user}    \n'
            + '  .::::::.888.    ::         :::`8888`.:.  {load}    \n'
            + ' ::::::::::.888   |         .::::::::::::  {reso}    \n'
            + ' ::::::::::::.8    |      .:8::::::::::::. {pkgs}    \n'
            + '.::::::::::::::.        .:888::::::::::::: {desktop} \n'
            + ':::::::::::::::88:.__..:88888:::::::::::`            \n'
            + ' ``.:::::::::::88888888888.88:::::::::`              \n'
            + '       ``:::_:` -- `` -`-` ``:_::::``                \n'
            + '                                                     \n'
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
        raise OSInfoError('Unable to open file: /proc/uptime')

    total_seconds = float(data[0])

    # Helper variables
    minute = 60
    hour = minute * 60
    day = hour * 24

    days = int(total_seconds / day)
    hours = int((total_seconds % day) / hour)
    minutes = int((total_seconds % hour) / minute)
    seconds = int(total_seconds % minute)

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
        raise OSInfoError('Unable to open file: /proc/loadavg')

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
    if distro == ('', '', ''):
        try:
            result = subprocess.check_output(['lsb_release', '-ds'])
            result = result.strip("\n\"")
        except subprocess.CalledProcessError:
            raise OSInfoError('Unable to execute lsb_release: ' +
                              str(sys.exc_info()))
    else:
        result = distro[0] + ' ' + distro[1] + ' ' + distro[2]

    return result

def get_distribution_name():
    """Returns distribution name."""

    distro = platform.linux_distribution()[0]
    if len(distro) == 0:
        try:
            distro = subprocess.check_output(['lsb_release', '-is'])
            distro = distro.strip()
        except subprocess.CalledProcessError:
            raise OSInfoError('Unable to execute lsb_release: ' +
                              str(sys.exc_info()))

    return distro.lower()

def get_username():
    """Returns the login name of the user."""

    return getpass.getuser()

def get_resolution():
    """Returns screen resolution using xrandr.

    Currently supports only single monitor setups.
    """

    try:
        output = subprocess.check_output(['xrandr'])
    except subprocess.CalledProcessError:
        raise OSInfoError('Unable to execute xrandr: ' +
                          str(sys.exc_info()))

    output = output.decode('utf-8')
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

    if (distro == 'fedora' or distro == 'suse' or
            distro == 'centos' or distro == 'redhat'):
        try:
            output = subprocess.check_output(['rpm', '-qa'])
        except subprocess.CalledProcessError:
            raise OSInfoError('Unable to execute rpm: ' +
                              str(sys.exc_info()))
    elif distro == 'debian' or distro == 'ubuntu' or distro == 'mint':
        try:
            output = subprocess.check_output(['dpkg', '-l'])
        except subprocess.CalledProcessError:
            raise OSInfoError('Unable to execute dpkg: ' +
                              str(sys.exc_info()))
    elif distro == 'arch':
        try:
            output = subprocess.check_output(['pacman', '-Q'])
        except subprocess.CalledProcessError:
            raise OSInfoError('Unable to execute pacman: ' +
                              str(sys.exc_info()))
    else:
        return 'Unable to count packages'

    output = output.decode('utf-8')
    output = output.split('\n')

    return str(len(output))

def get_desktop_environment():
    """Try to guess the current desktop environment"""
    desktop = os.environ.get('XDG_CURRENT_DESKTOP')
    if desktop is None:
        desktop = os.environ.get('DESKTOP_SESSION')
        if desktop is None:
            raise OSInfoError("Unable to get desktop environment")

    return desktop

def get_desktop_version(desktop):
    """Returns the desktop environment version string."""

    desktop = desktop.lower()

    if desktop == 'gnome':
        desktop = 'gnome-shell --version'
    elif desktop == 'kde':
        desktop = 'kde4-config --version'
    else:
        return "not available"

    command = desktop.split()

    try:
        output = subprocess.check_output(command)
    except subprocess.CalledProcessError as err:
        # gnome-session --version returns 1 instead of 0. The bug is fixed
        # in GNOME 3.7.3 but here's a hack to make this work with earlier
        # versions.
        output = err.output

    output = output.decode('utf-8')
    result = output.split()
    if len(result) > 2:
        return result[2]
    else:
        return result[1]

def print_info():
    """Print OS information"""
    logo = get_distro_logo(get_distribution_name())
    desktop = get_desktop_environment()
    info = {}
    info['uptime'] = "Uptime: " + get_uptime()
    info['kernel'] = "Kernel: " + get_kernel_version()
    info['host'] = "Hostname: " + get_hostname()
    info['distro'] = "Distribution: " + get_distribution_name()
    info['user'] = "User: " + get_username()
    info['load'] = "Loadavg: " + get_loadavg()
    info['reso'] = "Resolution: " + get_resolution()
    info['pkgs'] = "Installed packages: " \
        + get_number_of_installed_packages()
    info['desktop'] = "Desktop: " + desktop + " " \
        + get_desktop_version(desktop)

    print(logo.format(**info))


class OSInfoError(Exception):
    """Trivial OSInfo error."""
    pass

if __name__ == '__main__':

    try:
        print_info()
    except OSInfoError as err:
        raise err
