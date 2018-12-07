# UITableViewCell's contentView gets unwanted height==44 constraint

1. To Solve this issue, add these code:

   ```swift
    override func awakeFromNib() {
       super.awakeFromNib()
       self.contentView.autoresizingMask = UIViewAutoresizing.FlexibleHeight
    }

    self.tableView.estimatedRowHeight = 120
    self.tableView.rowHeight = UITableViewAutomaticDimension
   ```

2. UITableView insert animation crashed issue, to solve this issue:
   
   ```objective c
      dispatch_async(dispatch_get_main_queue(), ^{
            [self.tableView beginUpdates];
            [self.tableView insertRowsAtIndexPaths:@[[NSIndexPath indexPathForItem:1 inSection:0]] withRowAnimation:UITableViewRowAnimationFade];
            [self.tableView endUpdates];
        });
   ```

## References

[UITableViewCell's contentView gets unwanted “height==44” constraint
](https://stackoverflow.com/questions/26100053/uitableviewcells-contentview-gets-unwanted-height-44-constraint)