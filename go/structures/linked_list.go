package structures

import (
	"fmt"
)

type LinkedListNode struct {
	value int
	next  *LinkedListNode
}

type LinkedList struct {
	head *LinkedListNode
}

func (ll *LinkedList) AddToHead(data int) {
	if ll.head == nil {
		ll.head = &LinkedListNode{
			value: data,
			next:  nil,
		}
	} else {
		current := ll.head
		ll.head = &LinkedListNode{
			value: data,
			next:  current,
		}
	}
}

func (ll *LinkedList) AddToTail(val int) {
	newNode := &LinkedListNode{
		value: val,
		next:  nil,
	}

	if ll.head == nil {
		ll.head = newNode
		return
	}

	current := ll.head
	for current.next != nil {
		current = current.next
	}
	current.next = newNode
}

func (ll *LinkedList) RemoveHead() {
	if ll.head == nil {
		return
	}
	current := ll.head
	ll.head = current.next
}

func (ll *LinkedList) RemoveTail() {
	if ll.head == nil {
		return
	}
	if ll.head.next == nil {
		ll.head = nil
		return
	}

	current := ll.head
	for current.next.next != nil {
		current = current.next
	}
	current.next = nil
}

func (ll *LinkedList) Len() int {
	count := 0
	current := ll.head
	for current != nil {
		count++
		current = current.next
	}
	return count
}

func (ll *LinkedList) Print() {
	current := ll.head
	for current != nil {
		fmt.Printf("%d -> ", current.value)
		current = current.next
	}
	fmt.Println()
}
func (ll *LinkedList) ToArray() []int {
	if ll.head == nil {
		return nil
	}
	current := ll.head
	res := make([]int, 0)
	for current != nil {
		res = append(res, current.value)
		current = current.next
	}
	return res
}
