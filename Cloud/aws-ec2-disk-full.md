# Amazon EC2 - disk full

When you run `df`, the output is `/dev/xvda1    100%   /`. It means the disk space is full. You can use the following command to find big size files.

```
  sudo find / -type f -size +100M -exec ls -lh {} \;
```

Reference:[http://stackoverflow.com/questions/20031604/amazon-ec2-disk-full](http://stackoverflow.com/questions/20031604/amazon-ec2-disk-full)  
