#!/bin/bash
#
# q2ctf
#
# chkconfig: - 98 10
# description: Quake II "Capture The Flag" Server
# processname: q2ded
#
# taken from a connectiva RPM <aurelio@conectiva.com.br>.
# Modified for Mandrake by: Maxim Heijndijk <cchq@wanadoo.nl>
#
# Source function library
. /etc/rc.d/init.d/functions

NAME=q2ded
SERVER_NAME=`hostname -s`
PID=/var/run/${NAME}.pid
Q2_CONFIGDIR="/etc/quake2"

# Look for server.cfg
if [ -f "${Q2_CONFIGDIR}/ctf/server.cfg" ]; then

    if grep "^map[ ]" ${Q2_CONFIGDIR}/ctf/server.cfg; then

	SERVER_CFG="+exec server.cfg"

    else

	gprintf "No map found in \"${Q2_CONFIGDIR}/ctf/server.cfg\". Put a line \"map <quake2map>\" in \"server.cfg\". Aborting..."
	echo
	exit 0

    fi

fi

case "$1" in

    start)	gprintf "Starting Quake II \"Capture The Flag\" Server: "
		daemon /usr/games/${NAME} +set game ctf \
					  +set hostname ${SERVER_NAME} \
					  ${SERVER_CFG} &
		RETVAL=$?
		echo
		[ $RETVAL -eq 0 ] && touch /var/lock/subsys/${NAME}
		;;

    stop)	gprintf "Stopping Quake II \"Capture The Flag\" Server: "
		killproc ${NAME}
		killproc ${NAME}.bin
		RETVAL=$?
		echo
		[ $RETVAL -eq 0 ] && rm -f /var/lock/subsys/${NAME}
		;;

    status)	gprintf "Status Quake II \"Capture The Flag\" Server: "
		status ${NAME}
		RETVAL=$?
		;;

    restart)	$0 stop
    		$0 start
		RETVAL=$?
    		;;

    *)		gprintf "Usage: %s {start|stop|status|restart}"
		exit 1
		;;

esac

exit 0
