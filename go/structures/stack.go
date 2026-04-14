package structures

type Stack struct {
	values []int
}

func NewStack() *Stack {
	return &Stack{
		values: make([]int, 0),
	}
}

func (s *Stack) Push(n int) {
	s.values = append(s.values, n)
}

func (s *Stack) Peek() (int, bool) {
	if len(s.values) == 0 {
		return 0, false
	}
	length := len(s.values)
	return s.values[length-1], true
}

func (s *Stack) Pop() (int, bool) {
	length := len(s.values)
	if length == 0 {
		return 0, false
	}
	item := s.values[length-1]
	s.values = s.values[:length-1]
	return item, true
}

func (s *Stack) Len() int {
	return len(s.values)
}

func (s *Stack) IsEmpty() bool {
	return s.Len() == 0
}

func DeleteMiddleElement(myStack Stack) {

	length := myStack.Len()
	count := 0
	secondStack := NewStack()

	for count < length/2 {
		item, _ := myStack.Pop()
		secondStack.Push(item)
		count++
	}
	_, _ = myStack.Pop()

	for secondStack.Len() > 0 {
		item, _ := secondStack.Pop()
		myStack.Push(item)
	}

}

func DeleteMiddleElementRecursion(myStack Stack, n int) {
	length := myStack.Len()

	if n == length/2 {
		myStack.Pop()
		return
	}
	elem, _ := myStack.Pop()
	DeleteMiddleElementRecursion(myStack, n+1)
	myStack.Push(elem)
}
