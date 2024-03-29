import hashlib, binascii

class MerkleTree:
    """
        `The Merkle Tree is a special kind of Binary Tree that allows the user to prevent 
        information malleability and preserve integrity by using cryptographically secure
        hash functions. By providing leaves you create a root by concatination and hashingself.
        If the root is mutated it means that the data inside the leaves was changed. You can also
        derive cryptographic proofs that a piece of data is inside the tree`

        Comments:
           Complexities - This part can be improved by doing couple of modifications 
    """


    class __Node:

        def __init__(self, item=None, left=None, right=None):
            """
            `Merkle Node constructor. Used for storing the left and right node pointersself.`

            Args:
                item (bytes): Bytes object that represents the hashed value that resides in the current node
                left (Node): Reference to the left subtree or a None value if current node is leaf
                right (Node): Reference to the right subtree or a None value if current node is leaf
            """
            self.left = left
            self.right = right
            self.__value = item

        @property
        def value(self):
            return self.__value

        @value.setter
        def value(self, value):
            self.__value = value

        def __str__(self):
            return 'Value: {0}'.format(self.value)
        
        def __repr__(self):
            return self.__str__() + '\n\t' + self.left.__repr__() + '\n\t' + self.right.__repr__()

    
    def __init__(self,
                 iterable,
                 digest_delegate=lambda x: str(x)):
        """
            `Merkle Tree constructor`
        
            Args:
                iterable (list_iterator): The collection you want to create the root from
                digest_delegate (function): ~
                  ~ A delegate (reference to function) that returns the digest of a passed in argument
        """
        self.digest = digest_delegate
        self.__root = self.build_root(iterable)
  
    @property
    def root(self):
        return self.__root

    def build_root(self, iterable):
        """
            `This method builds a Merkle Root from the passed in iterable.
             After the data is preprocessed, it calls the internal __build_root
             function to build the actual Merkle Root.`
            
            Args:
                iterable (list_iterator): The collection you want to create the root from
            
            Returns:
                Node: The newly built root of the Merkle Tree
        """
        # TODO: Implement this method
        # Try implementing this method yourself
        size = len(iterable)

        # When size is 1 the root is the only node that is left
        if size == 1:
            return iterable[0]

        # Double the last node if the size is odd
        if size % 2 != 0:
            iterable.extend(iterable[-1:])

        # Iterate over the collection and create the upper layers till the root is reached
        # Keep references for each node to its children
        parents = []

        i = 0
        while i < size:
            left = iterable[i]
            right = iterable[i + 1]

            if isinstance(left, self.__Node):
                node = self.__Node(self.digest(left.value + right.value), left, right)
                parents.append(node)
            else:
                hashed_left = self.digest(left)
                hashed_right = self.digest(right)
                node = self.__Node(self.digest(hashed_left + hashed_right), None, None)
                parents.append(node)
            
            i += 2

        # Return the root
        return self.build_root(parents)

    # def hash_data(self, data):
    #     sha256hash = hashlib.sha256(str(data).encode('utf-8')).digest()
    #     return binascii.hexlify(sha256hash)


    def contains(self, value):
        """
            `The contains method checks whether the item passed in as an argument is in the
            tree and returns True/False. It is used only externally. It's internal equivalent
            is __find`

            Args:
                value (object): The value you are searching for

            Returns:
                bool: The result of the search

            Complexity:
                O(n)
        """
        if value is None or self.root is None:
            return False

        hashed_value = self.digest(value)

        return self.__find(self.root, hashed_value) is not None 

    def __find(self, node, value):
        """
            `Find is the internal equivalent of the contains method`

            Args:
                value (object): The value you are searching for

            Returns:
                bool: The result of the search

            Complexity:
                O(n)
        """
        if node is None:
            return None

        if node.value == value:
            return node
        
        return self.__find(node.left, value) or self.__find(node.right, value)

    def request_proof(self, value):
        """
            `The request_proof method provides to the caller a merkle branch in order to prove
            that the integrity of the data is in tact. The caller can use the same digest and 
            verify it himself`

            Args:
               value (object) - The item you want proof for

            Returns:
               list - Python list containing the merkle branch (proof) in the form of tuples

            Throws:
                Exception - On invalid value or one that is not contained in the tree
        """
        # TODO: Implement this method
        # Try implementing this method yourself. It is not mandatory though. There is a 
        # step by step solution in the exercise document

        # Hash the value
        
        # Check if it is contained within the tree

        # Start building the proof

        # Traverse left and right to find the correct leaf node
    
        # If the leaf was found in the left subtree -> add the right node to the proof list

        # If it was both found on the left and on the right -> it means that left and right values are identical
        # Do not add to the list

        # Create tuple with the node value and the position it was found on
        # 0 for right node and 1 for left node e.g (1, node.left)    

        # Append to the list

        
    def dump(self, indent=0):
        
        if self.root is None:
            return

        self.__print(self.root, indent)

    def __print(self, node, indent):
        
        if node is None:
            return

        print('{0}Node: {1}'.format(' '*indent, node.value))    
        self.__print(node.left, indent+2)
        self.__print(node.right, indent+2)

    def __contains__(self, value):
        hashed_value = self.digest(value)
        return self.__find(self.root, hashed_value)
