# Real ETH addr
0xa7076edf241de34c203b835c157e0fff233db065


# Try to deploy this...
```
pragma solidity ^0.4.0;
pragma experimental ABIEncoderV2;

contract MyContract {
    bytes[] arr;

    function set(string memory x) public {
        bytes memory b = bytes(x);
        arr.push(b);
    }

    function get() view public returns (bytes[] memory) {
        uint n = arr.length;
        bytes[] memory result = new bytes[](n);
        for (uint i = 0; i < n; i++) {
            result[i] = arr[i];
        }
        
        return result;
    }
}
```
