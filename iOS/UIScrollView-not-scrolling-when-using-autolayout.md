# UIScrollView not scrolling when using autolayout
If you're using autolayout, you need to set contentSize in viewDidLayoutSubviews in order for it to be applied after the autolayout completes.
http://stackoverflow.com/questions/2824435/uiscrollview-not-scrolling
