(setq l (list 1 2 3 4 5 6 7))

(defun element(n)
	(nth n l))

(defvar a)
(setq a (read))
(terpri)
(format t "Index ~d element of list is ~d" a (element a))