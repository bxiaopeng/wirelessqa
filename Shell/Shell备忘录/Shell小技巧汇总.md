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



# shell中如何进行一段代码的注释

```
:<<!EOF!
cp ./a.txt ./b.txt
mkdir -p {1,2,3}/{4,5,6}
echo "ok"
!EOF!
```
也把要注释的shell整体变成一个函数来达到不让执行的目的
```
notExce(){
cp ./a.txt ./b.txt
mkdir -p {1,2,3}/{4,5,6}
echo "ok"
}
```