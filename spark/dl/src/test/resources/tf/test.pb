
4
PlaceholderPlaceholder*
dtype0*
shape: 
a
VariableConst*A
value8B6
"(��L>��L>��L>��L>��L>��L>��L>��L>��L>��L>*
dtype0
I
Variable/readIdentityVariable*
T0*
_class
loc:@Variable
_

Variable_1Const*=
value4B2
"(���=���=���=���=���=���=���=���=���=���=*
dtype0
O
Variable_1/readIdentity
Variable_1*
_class
loc:@Variable_1*
T0
[
MatMulMatMulPlaceholderVariable/read*
transpose_b( *
T0*
transpose_a( 
K
BiasAddBiasAddMatMulVariable_1/read*
T0*
data_formatNHWC

TanhTanhBiasAdd*
T0
c

Variable_2Const*A
value8B6
"(��L>��L>��L>��L>��L>��L>��L>��L>��L>��L>*
dtype0
O
Variable_2/readIdentity
Variable_2*
_class
loc:@Variable_2*
T0
;

Variable_3Const*
valueB*���=*
dtype0
O
Variable_3/readIdentity
Variable_3*
T0*
_class
loc:@Variable_3
X
MatMul_1MatMulTanhVariable_2/read*
transpose_b( *
transpose_a( *
T0
L
outputBiasAddMatMul_1Variable_3/read*
T0*
data_formatNHWC