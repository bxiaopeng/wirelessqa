# Base Shell等待菊花转呀转

### Function: 

```
spinner()
{
    local pid=$!
    local delay=0.75
    local spinstr='|/-\'
    while [ "$(ps a | awk '{print $1}' | grep $pid)" ]; do
        local temp=${spinstr#?}
        printf " [%c]  " "$spinstr"
        local spinstr=$temp${spinstr%"$temp"}
        sleep $delay
        printf "\b\b\b\b\b\b"
    done
    printf "    \b\b\b\b"
}

```

### 用法：

```
(a_long_running_task) & spinner
```

### 效果:

[ | ] [ / ] [ — ] [ / ] [ | ] 转呀转呀转


From : http://stackoverflow.com/questions/12498304/using-bash-to-display-a-progress-working-indicator/12498305#12498305