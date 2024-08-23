# Bytecode for the expression s[a] += b

import dis

dis.dis('s[a] += b')

# 0           0 RESUME                   0

# 1           2 LOAD_NAME                0 (s)
#             4 LOAD_NAME                1 (a)
#             6 COPY                     2
#             8 COPY                     2
#             10 BINARY_SUBSCR                      # Put the value of s[a] on TOS (Top Of Stack).
#             14 LOAD_NAME                2 (b)
#             16 BINARY_OP               13 (+=)    # Perform TOS += b. This succeeds if TOS refers to a mutable object (it’s a list, in Example 2-17)
#             20 SWAP                     3
#             22 SWAP                     2
#             24 STORE_SUBSCR                       # Assign s[a] = TOS. This fails if s is immutable (the t tuple in Example 2-17).
#             28 RETURN_CONST             0 (None)