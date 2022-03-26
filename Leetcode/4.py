def findMedianSortedArrays(nums1, nums2):
        target_index = int((len(nums1) + len(nums2)) / 2)
        #print('target_index: {}'.format(target_index))
        i, j, count = 0, 0, 0
        current_item = min(nums1[0], nums2[0])
        while count < target_index and len(nums1)-1 > i and len(nums2)-1 > j:
            pre_item = current_item
            if nums1[i] < nums2[j]:
                i = i + 1
            else:
                j = j + 1

            current_item = min(nums1[i], nums2[j])
            count = count + 1

        #print('count: {}'.format(count))
        #print('i: {}'.format(i))
        #print('j: {}'.format(j))
        if len(nums1)-1 == i:
            while count < target_index and len(nums2)-1 > j:
                pre_item = current_item

                current_item = nums2[j]
                j = j + 1
                count = count + 1

        elif len(nums2)-1 == j:
            while count < target_index and len(nums1)-1 > i:
                pre_item = current_item

                current_item = nums1[i]
                i = i + 1
                count = count + 1


        if (len(nums1) + len(nums2)) % 2 == 0:
            #print('pre_item: {}    current_item:{}'.format(pre_item, current_item))
            return (pre_item + current_item) / 2
        else:
            return current_item


if __name__ == '__main__':
    nums1 = [1]
    nums2 =  [2, 3, 4]
    result = findMedianSortedArrays(nums1, nums2)
    print('result: {}'.format(result))