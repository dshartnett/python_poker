# David H
# 2015-04-28

# <re> = <r0>, <f2><fc><re><re>

# <f2> = "if"

# <fc> = <f7><fc><fc>, <f8><s><s>, <f8><c><c>, <f9><c><c>

# <f7> ::= "or", "and"
# <f8> ::= "==", "!="
# <f9> ::= ">1", "<1"

# <s> ::= s1, s2, s3, s4, s5, <s0>
# <c> ::= c1, c2, c3, c4, c5, <c0>

# <r0> ::= 0,1,2,3,4,5,6,7,8,9
# <s0> ::= 1,2,3,4
# <c0> ::= 1,2,3,4,5,6,7,8,9,10,11,12,13

class BNGrammar:

	s = [0]*5
	c = [0]*5
	r0 = [0,1,2,3,4,5,6,7,8,9]

	def _r(self, i):
		return self.r0[i]

	def _f2(self, fc, re1, re2):
		if fc: return re1
		else: return re2

	re = [_r, _f2]
