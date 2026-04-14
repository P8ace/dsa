package structures

type Queue struct {
	values []int
}

func NewQueue() *Queue {
	return &Queue{
		values: make([]int, 0),
	}
}

func (q *Queue) Push(n int) {
	q.values = append(q.values, n)
}

func (q *Queue) Pop() (int, bool) {
	if q.Len() == 0 {
		return 0, false
	}
	elem := q.values[0]
	q.values = q.values[1:]
	return elem, true
}

func (q *Queue) Len() int {
	return len(q.values)
}

func (q *Queue) IsEmpty() bool {
	return q.Len() == 0
}
