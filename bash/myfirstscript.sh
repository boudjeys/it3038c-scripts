echo Machine Type: $MACHTYPE
echo Hostname: $HOSTNAME
echo Working Dir: $PWD
echo Session length: $SECONDS
echo Home Dir: $HOME

a=$(ip a | grep 'noprefixroute ens192'| awk '{print $2}')
echo my IP is $a
