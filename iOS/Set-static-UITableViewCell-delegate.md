# Set static UITableViewCell delegate


```objective-c
- (UITableViewCell *)tableView:(UITableView *)tableView cellForRowAtIndexPath:(NSIndexPath *)indexPath {
    UITableViewCell *cell = [super tableView:tableView cellForRowAtIndexPath:indexPath];
    if (indexPath.row == 0) {
        ((MyTableViewViewCell *)cell).delegate = self;
    }
    return cell;
}
```
