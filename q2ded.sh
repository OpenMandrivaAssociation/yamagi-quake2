#!/bin/bash
#
# q2ded
#
# chkconfig: - 98 10
# description: Quake II Dedicated Server
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
if [ -f "${Q2_CONFIGDIR}/baseq2/server.cfg" ]; then

    if grep "^map[ ]" ${Q2_CONFIGDIR}/baseq2/server.cfg; then

	SERVER_CFG="+exec server.cfg"

    else

	echo -e "No map found in \"${Q2_CONFIGDIR}/baseq2/server.cfg\". Put a line \"map <quake2map>\" in \"server.cfg\". Aborting..."
	echo
	exit 0

    fi

fi

case "$1" in

    start)	gprintf "Starting Quake II Dedicated Server: "
		daemon /usr/games/${NAME} +set hostname ${SERVER_NAME} \
					  ${SERVER_CFG} &
		RETVAL=$?
		echo
		[ $RETVAL -eq 0 ] && touch /var/lock/subsys/${NAME}
		;;

    stop)	gprintf "Stopping Quake II Dedicated Server: "
		killproc ${NAME}
		killproc ${NAME}.bin
		RETVAL=$?
		echo
		[ $RETVAL -eq 0 ] && rm -f /var/lock/subsys/${NAME}
		;;

    status)	gprintf "Status Quake II Dedicated Server: "
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
