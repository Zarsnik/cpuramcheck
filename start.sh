#!/bin/bash
cp chkd.py /usr/local/sbin/chkd.py
cp chkd.service /etc/systemd/system/chkd.service
if [[ -e /etc/systemd/system/chkd.service ]] && [[ -e /usr/local/sbin/chkd.py ]]; then
	systemctl enable chkd.service && systemctl start chkd.service
fi
