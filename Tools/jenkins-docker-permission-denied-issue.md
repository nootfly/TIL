# Jenkins docker run permission errors

To solve `Permission denied - /var/jenkins_home/copy_reference_file.log` issue,

If the directory is empty:
`sudo chown 1000 volume_dir`

If the directory already contains files:
`sudo chown -R 1000 volume_dir`

Reference:[https://github.com/jenkinsci/docker/issues/177](https://github.com/jenkinsci/docker/issues/177)
