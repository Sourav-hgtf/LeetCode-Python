from typing import List

class Solution:
    def resultArray(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        n = len(nums)

        # tree[node] = [product % k, counts of prefix products]
        tree = [[1, [0] * k] for _ in range(4 * n)]

        def merge(left, right):
            prod1, cnt1 = left
            prod2, cnt2 = right

            prod = (prod1 * prod2) % k
            cnt = cnt1[:]

            for r in range(k):
                new_r = (prod1 * r) % k
                cnt[new_r] += cnt2[r]

            return [prod, cnt]

        def build(node, l, r):
            if l == r:
                value = nums[l] % k
                tree[node] = [value, [0] * k]
                tree[node][1][value] = 1
                return

            mid = (l + r) // 2
            build(node * 2, l, mid)
            build(node * 2 + 1, mid + 1, r)

            tree[node] = merge(tree[node * 2], tree[node * 2 + 1])

        def update(node, l, r, index, value):
            if l == r:
                value %= k
                tree[node] = [value, [0] * k]
                tree[node][1][value] = 1
                return

            mid = (l + r) // 2

            if index <= mid:
                update(node * 2, l, mid, index, value)
            else:
                update(node * 2 + 1, mid + 1, r, index, value)

            tree[node] = merge(tree[node * 2], tree[node * 2 + 1])

        def query(node, l, r, ql, qr):
            if ql <= l and r <= qr:
                return tree[node]

            mid = (l + r) // 2

            if qr <= mid:
                return query(node * 2, l, mid, ql, qr)

            if ql > mid:
                return query(node * 2 + 1, mid + 1, r, ql, qr)

            left = query(node * 2, l, mid, ql, qr)
            right = query(node * 2 + 1, mid + 1, r, ql, qr)

            return merge(left, right)

        build(1, 0, n - 1)

        result = []

        for index, value, start, x in queries:
            update(1, 0, n - 1, index, value)

            node = query(1, 0, n - 1, start, n - 1)
            result.append(node[1][x])

        return result