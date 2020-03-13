;;;;;;;;;;;;;;;
;; Questions ;;
;;;;;;;;;;;;;;;

; Scheme

(define (cddr s)
  (cdr (cdr s)))

(define (cadr s)
  'YOUR-CODE-HERE
  (car (cdr s))
)

(define (caddr s)
  'YOUR-CODE-HERE
  (car (cdr (cdr s)))
)

(define (unique s)
  'YOUR-CODE-HERE
  (cond
    ((null? s) '( ))
    ((eq? (car s) s)
    (else (contains? (cdr-stream list) s)))
  )
)

(define (cons-all first rests)
  'replace-this-line)

;; List all ways to make change for TOTAL with DENOMS
(define (list-change total denoms)
  'YOUR-CODE-HERE
  )

; Tail recursion

(define (replicate x n)
  'YOUR-CODE-HERE
  )

(define (accumulate combiner start n term)
  'YOUR-CODE-HERE
)

(define (accumulate-tail combiner start n term)
  'YOUR-CODE-HERE
)


; Macros

(define-macro (list-of map-expr for var in lst if filter-expr)
  'YOUR-CODE-HERE
)
