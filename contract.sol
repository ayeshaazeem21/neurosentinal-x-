// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract FraudChain {
    string[] public fraudHashes;

    function storeHash(string memory hashValue) public {
        fraudHashes.push(hashValue);
    }

    function getAllHashes() public view returns (string[] memory) {
        return fraudHashes;
    }
}