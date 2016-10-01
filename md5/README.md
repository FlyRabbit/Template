# MD5 #

## update ##
append string to old string

## reset ##
reset update buf and toString buf

## toString ##
return a md5 string
after you used toString function ,the md5buf would save current md5 string , although you reseted.

## md5buf ##
This one only change when toString function execute,
md5buf will get current md5 string
