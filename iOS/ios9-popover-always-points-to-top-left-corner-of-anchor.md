#iOS 9 PopOver points to top-left corner of anchor

The fix is from stackoverflow: http://stackoverflow.com/questions/32666214/ios9-popover-always-points-to-top-left-corner-of-anchor

```
- (void)prepareForSegue:(UIStoryboardSegue *)segue sender:(id)sender {
    if ([segue.identifier isEqualToString:@"BalanceInfo"]) {
        UIViewController *infoVC = segue.destinationViewController;
        infoVC.preferredContentSize = CGSizeMake(351, 286);
        infoVC.popoverPresentationController.sourceRect = self.balanceInfoButton.bounds;

    }
}
```
