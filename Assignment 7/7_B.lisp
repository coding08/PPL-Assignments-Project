(print "Find the factorial of the number")
(defvar a 1)
(defvar ans 1)
(setq a (read))
(loop for i from 1 to a 
	do(
		setq ans (* ans i)))

(format t "~%Factorial of number using iteration is : ~d " ans)

;(defvar ans1 1 )
(defun factorial(n)
	(if (= n 0)
		1 
		(* n (factorial(- n 1))))
)
(defvar ans1 (factorial a))
(format t "~%Factorial of number using recursion is : ~d " ans1)