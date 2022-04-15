// javaScript는 함수 선언시에 앞에 new를 붙여줘야 함
var mergeTwoLists = function(list1, list2) {
    let answer = new ListNode()
    let root = answer
    
    while(list1 && list2){
        if(list1.val < list2.val){
            answer.next = new ListNode(list1.val)
            answer = answer.next
            list1 = list1.next
        }else{
            answer.next = new ListNode(list2.val)
            answer = answer.next
            list2 = list2.next
        }
    }
    if(list1){
        answer.next = list1
    }else if(list2){
        answer.next = list2
    }
    
    return root.next
};

// 재귀 풀이
// 이 풀이에서는 함수 앞에 new를 붙이지 않아도 잘 작동함.. 재귀인지 아닌지의 차이인지..
var mergeTwoLists = function(list1, list2) {
    if (!list1 || !list2) {
        return list1 || list2;
    }
    if (list1.val < list2.val) {
        list1.next = mergeTwoLists(list1.next, list2);
        return list1;
    }
    list2.next = mergeTwoLists(list1, list2.next);
    return list2;
};


