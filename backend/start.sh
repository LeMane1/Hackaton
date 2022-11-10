#!/bin/bash

cp vtb.service  /etc/systemd/system/vtb.service
systemctl daemon-reload
systemctl restart vtb.service
systemctl enable vtb.service   #добавить в автозагрузку