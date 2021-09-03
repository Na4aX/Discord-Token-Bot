curl 'https://bscscan.com/token/0x40b165fd5ddc75ad0bddc9add0adabff5431a975' 2>  /dev/null | grep -shoP "number of holders .*? " | uniq | cut -d ' ' -f 4
