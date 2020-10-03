
public class MyLinkedList<E> {

	Node<E> head;

	void add(E data) {
		Node<E> toAdd = new Node<E>(data);

		if (isEmpty()) {
			head = toAdd;
			return;
		}

		Node<E> temp = head;
		while (temp.next != null) {
			temp = temp.next;
		}

		temp.next = toAdd;
	}

	private String outOfBoundsMsg(int index) {
		return "Index: " + index;
	}

	E get(int index) {
		if (index >= size() || index < 0)
			throw new IndexOutOfBoundsException(outOfBoundsMsg(index));
		else {
			Node<E> temp = head;
			int c = 0;
			while (c < index) {
				temp = temp.next;
				c++;
			}
			return temp.data;
		}
	}

	void add(E val, int index) {
		Node<E> newNode = new Node<E>(val);
		if (index > size() || index < 0)
			throw new IndexOutOfBoundsException(outOfBoundsMsg(index));
		else if (index == 0) {
			newNode.next = head;
			head = newNode;
		} else if (index == size()) {
			Node<E> temp = head;
			while (temp.next != null) {
				temp = temp.next;
			}

			temp.next = newNode;

		} else {
			Node<E> temp = head;
			Node<E> prev = null;
			while (temp != null) {
				if (index == 0) {
					prev.next = newNode;
					newNode.next = temp;
				}
				index--;
				prev = temp;
				temp = temp.next;
			}
		}
	}

	void set(E val, int index) {
		Node<E> newNode = new Node<E>(val);
		if (index >= size() || index < 0)
			throw new IndexOutOfBoundsException(outOfBoundsMsg(index));
		else if (index == 0) {
			head.data = val;
		} else {
			Node<E> temp = head;
			Node<E> prev = null;
			while (temp != null) {
				if (index == 0) {
					prev.next.data = val;
					newNode.next = temp;
				}
				index--;
				prev = temp;
				temp = temp.next;
			}
		}
	}

	void remove() {
		head = head.next;
	}

	void remove(int index) {
		if (index >= size() || index < 0)
			throw new IndexOutOfBoundsException(outOfBoundsMsg(index));
		else if (index == 0) {
			head = head.next;
		} else {
			Node<E> temp = head;
			Node<E> prev = null;
			while (temp != null) {
				if (index == 0) {
					prev.next = temp.next;
				}
				index--;
				prev = temp;
				temp = temp.next;
			}
		}

	}

	int size() {
		if (isEmpty())
			return 0;
		else {
			Node<E> temp = head;
			int c = 0;
			while (temp != null) {
				temp = temp.next;
				c++;
			}
			return c;
		}
	}

	boolean isEmpty() {
		return head == null;
	}

	void display() {
		Node<E> temp = head;
		while (temp != null) {
			System.out.print(temp.data + " ");
			temp = temp.next;
		}
	}

	static class Node<E> {
		E data;
		Node<E> next;

		public Node(E data) {
			this.data = data;
			next = null;
		}
	}
}
