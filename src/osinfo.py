#!/usr/bin/env python
#
#   osinfo.py
#
#   Prints miscellaneous information about linux host.
#
#   Licence: GPLv3 (https://www.gnu.org/licenses/gpl.txt)
#   Author: Janne Haapsaari <haaja@iki.fi>
#


def get_distro_logo(distro='default'):
    """ Function returns ascii representation for distro logo.

    Keyword arguments:
        distro -- name of the linux distribution
    """

    logo = {
        'ubuntu':   "                                               \n"
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
        'fedora':   '                                               \n'
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
        'mint':     '                                               \n'
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
        'debian':   '                                               \n'
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
        'arch':     '                                               \n'
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
        'default':  '                                               \n'
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


if __name__ == '__main__':
    print(get_distro_logo('debian'))
    print(get_distro_logo('fedora'))
    print(get_distro_logo('ubuntu'))
    print(get_distro_logo('mint'))
    print(get_distro_logo('rommikola'))
    print(get_distro_logo())
    print("Uptime: " + get_uptime())
