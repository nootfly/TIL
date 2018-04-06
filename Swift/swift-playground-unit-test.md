# Swift playground unit test

1. Create a unit test

```swift
import Foundation
import XCTest


public class UnitTests: XCTestCase {

    func testFindIndex() {
        XCTAssertEqual(Test.printFindIndexResult(" ", ""), "Position: N/A")
    }
}
```    

2. In swift playground run `UnitTests.defaultTestSuite.run()`