package structures

import "fmt"

type DoublyLinkedListNode struct {
	value int
	next  *DoublyLinkedListNode
	prev  *DoublyLinkedListNode
}

type DoublyLinkedList struct {
	head *DoublyLinkedListNode
	tail *DoublyLinkedListNode
}

func (dll *DoublyLinkedList) AddToHead(val int) {
	if dll.head == nil {
		newNode := &DoublyLinkedListNode{
			value: val,
			next:  nil,
			prev:  nil,
		}
		dll.head = newNode
		dll.tail = newNode
		return
	}

	current := dll.head
	newNode := &DoublyLinkedListNode{
		value: val,
		next:  current.next,
		prev:  nil,
	}
	dll.head = newNode
}

func (dll *DoublyLinkedList) AddToTail(val int) {
	if dll.tail == nil {
		newNode := &DoublyLinkedListNode{
			value: val,
			next:  nil,
			prev:  nil,
		}
		dll.tail = newNode
		dll.head = newNode
		return
	}
	current := dll.tail
	newNode := &DoublyLinkedListNode{
		value: val,
		next:  nil,
		prev:  current,
	}
	current.next = newNode
	dll.tail = newNode
}

func (dll *DoublyLinkedList) RemoveHead() {
	if dll.head == nil {
		return
	}
	current := dll.head
	dll.head = current.next
	dll.head.prev = nil

	// cleanup
	current.next = nil
	current.prev = nil
}

func (dll *DoublyLinkedList) RemoveTail() {
	if dll.tail == nil {
		return
	}
	current := dll.tail
	dll.tail = current.prev
	dll.tail.next = nil

	// cleanup
	current.next = nil
	current.prev = nil

}

func (dll *DoublyLinkedList) Len() int {
	count := 0
	current := dll.head

	for current != nil {
		count++
		current = current.next
	}
	return count
}

func (dll *DoublyLinkedList) Print() {
	if dll.head == nil {
		fmt.Println()
		return
	}
	current := dll.head
	for current != nil {
		fmt.Printf("%d -> ", current.value)
		current = current.next
	}
	fmt.Println()
}

func (dll *DoublyLinkedList) ToArray() []int {
	if dll.head == nil {
		return nil
	}
	current := dll.head
	res := make([]int, 0)
	for current != nil {
		res = append(res, current.value)
		current = current.next
	}
	return res
}
