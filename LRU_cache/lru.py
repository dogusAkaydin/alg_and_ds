import sys
class ListNode:

    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None

class LRU:

    def __init__(self, n_max):
        self.cache_dict = {}
        self.llh = ListNode(None, None)
        self.llt = self.llh
        self.n_max = n_max
        self.n = 0

    def put(self, key, val=None):
        if key and key in self.cache_dict:
        # Update the value of a given key:
            prev = self.cache_dict[key]
            update = prev.next
            print('(key={}, val={}) will be updated with val={}.'.format(update.key, update.val, val))
            if update.next: # The updated item is not MRU
                print('Evicting the old record, making the updated one MRU.')
                evict = update
                prev.next = evict.next
                self.cache_dict[evict.next.key]= prev
                del self.cache_dict[evict.key]
                del evict

                curr = ListNode(key, val)
                self.llt.next = curr
                self.cache_dict[key]= self.llt
                self.llt = curr
            else: # The updated item already MRU
                update.val = val
        else:
            if self.n < self.n_max:
                # Keep adding new items
                self.n += 1
                curr = ListNode(key, val)
                self.llt.next = curr
                self.cache_dict[key]= self.llt
                self.llt = curr

            elif self.n == self.n_max:
                # Evict the  LRU and put the new item as MRU
                prev = self.llh
                evict = prev.next
                print('n is maxed. Evicting LRU:', evict.key, evict.val)
                prev.next = evict.next
                self.cache_dict[evict.next.key]= prev
                del self.cache_dict[evict.key]
                del evict

                curr = ListNode(key, val)
                self.llt.next = curr
                self.cache_dict[key]= self.llt
                self.llt = curr

    def get(self, key):
        if key and key in self.cache_dict:
        # Update the value of a given key:
            prev = self.cache_dict[key]
            check = prev.next
            if check.next: # The item is not MRU
                print('Making the checked record MRU.')
                prev.next = check.next
                self.cache_dict[check.next.key]= prev
                self.llt.next = check
                self.cache_dict[key]= self.llt
                self.llt = check
                check.next = None
            return check.val
        else:
            return None

    def showList(self):
        node = self.llh
        while node:
            print(node.val)
            node = node.next

    def showDict(self):
        for key in self.cache_dict:
            print(key, self.cache_dict[key].key, self.cache_dict[key].val)
