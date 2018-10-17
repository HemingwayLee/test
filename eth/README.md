# Real ETH addr
0xa7076edf241de34c203b835c157e0fff233db065


# Try to deploy this...
```
pragma solidity ^0.4.0;

contract MyContract {
    bytes32[] arr;

    function set(bytes32 x) public {
        arr.push(x);
    }

    function get() view public returns (bytes32[] memory) {
        uint n = arr.length;
        bytes32[] memory result = new bytes32[](n);
        for (uint i = 0; i < n; i++) {
            result[i] = arr[i];
        }
        
        return result;
    }
}
```