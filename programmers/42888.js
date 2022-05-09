function solution(record) {
    members = {}
    records = record.map(order => order.split(' '))
    records.map(order => {
        if(order[0] === 'Enter' || order[0] === 'Change'){
            members[order[1]] = order[2]
        }
    })

    result = []
    records.map(order => {
        if(order[0] === 'Enter'){
            result.push(members[order[1]]+"님이 들어왔습니다.")
        }else if(order[0] === 'Leave'){
            result.push(members[order[1]]+"님이 나갔습니다.")
        }
    })

    return result
}