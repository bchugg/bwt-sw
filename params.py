import numpy as np

#Parameters file

#Use BLOSUM50 as the scoring matrix
score_index = ['A','R','N','D','C','Q','E','G','H','I','L','K','M',
 				'F','P','S','T','W','Y','V','B','J','Z','X','*']

blosum = np.matrix([
	[5,-2,-1,-2,-1,-1,-1,0,-2,-1,-2,-1,-1,-3,-1,1,0,-3,-2,0,-2,-2,-1,-1,-5],
	[-2,7,-1,-2,-4,1,0,-3,0,-4,-3,3,-2,-3,-3,-1,-1,-3,-1,-3,-1,-3,0,-1,-5],
	[-1,-1,7,2,-2,0,0,0,1,-3,-4,0,-2,-4,-2,1,0,-4,-2,-3,5,-4,0,-1,-5],
	[-2,-2,2,8,-4,0,2,-1,-1,-4,-4,-1,-4,-5,-1,0,-1,-5,-3,-4,6,-4,1,-1,-5],
	[-1,-4,-2,-4,13,-3,-3,-3,-3,-2,-2,-3,-2,-2,-4,-1,-1,-5,-3,-1,-3,-2,-3,-1,-5],
	[-1,1,0,0,-3,7,2,-2,1,-3,-2,2,0,-4,-1,0,-1,-1,-1,-3,0,-3,4,-1,-5],
	[-1,0,0,2,-3,2,6,-3,0,-4,-3,1,-2,-3,-1,-1,-1,-3,-2,-3,1,-3,5,-1,-5],
	[0,-3,0,-1,-3,-2,-3,8,-2,-4,-4,-2,-3,-4,-2,0,-2,-3,-3,-4,-1,-4,-2,-1,-5],
	[-2,0,1,-1,-3,1,0,-2,10,-4,-3,0,-1,-1,-2,-1,-2,-3,2,-4,0,-3,0,-1,-5],
	[-1,-4,-3,-4,-2,-3,-4,-4,-4,5,2,-3,2,0,-3,-3,-1,-3,-1,4,-4,4,-3,-1,-5],
	[-2,-3,-4,-4,-2,-2,-3,-4,-3,2,5,-3,3,1,-4,-3,-1,-2,-1,1,-4,4,-3,-1,-5],
	[-1,3,0,-1,-3,2,1,-2,0,-3,-3,6,-2,-4,-1,0,-1,-3,-2,-3,0,-3,1,-1,-5],
	[-1,-2,-2,-4,-2,0,-2,-3,-1,2,3,-2,7,0,-3,-2,-1,-1,0,1,-3,2,-1,-1,-5],
	[-3,-3,-4,-5,-2,-4,-3,-4,-1,0,1,-4,0,8,-4,-3,-2,1,4,-1,-4,1,-4,-1,-5],
	[-1,-3,-2,-1,-4,-1,-1,-2,-2,-3,-4,-1,-3,-4,10,-1,-1,-4,-3,-3,-2,-3,-1,-1,-5],
	[1,-1,1,0,-1,0,-1,0,-1,-3,-3,0,-2,-3,-1,5,2,-4,-2,-2,0,-3,0,-1,-5],
	[0,-1,0,-1,-1,-1,-1,-2,-2,-1,-1,-1,-1,-2,-1,2,5,-3,-2,0,0,-1,-1,-1,-5],
	[-3,-3,-4,-5,-5,-1,-3,-3,-3,-3,-2,-3,-1,1,-4,-4,-3,15,2,-3,-5,-2,-2,-1,-5],
	[-2,-1,-2,-3,-3,-1,-2,-3,2,-1,-1,-2,0,4,-3,-2,-2,2,8,-1,-3,-1,-2,-1,-5],
	[0,-3,-3,-4,-1,-3,-3,-4,-4,4,1,-3,1,-1,-3,-2,0,-3,-1,5,-3,2,-3,-1,-5],
	[-2,-1,5,6,-3,0,1,-1,0,-4,-4,0,-3,-4,-2,0,0,-5,-3,-3,6,-4,1,-1,-5],
	[-2,-3,-4,-4,-2,-3,-3,-4,-3,4,4,-3,2,1,-3,-3,-1,-2,-1,2,-4,4,-3,-1,-5],
	[-1,0,0,1,-3,4,5,-2,0,-3,-3,1,-1,-4,-1,0,-1,-2,-2,-3,1,-3,5,-1,-5],
	[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-5],
	[-5,-5,-5,-5,-5,-5,-5,-5,-5,-5,-5,-5,-5,-5,-5,-5,-5,-5,-5,-5,-5,-5,-5,-5,1]])


seq = ("METDLAEMPEKGVLSSQDSPHFQEKSTEEGEVAALRLTARSQAAAAAAAPGSRSLRGVHV"
	"PPPLHPAPAREEIKSTCSLKACFSLSLTLTYYRTAFLLSTENEGNLHFQCPSDVETRPQS"
	"KDSTSVQDFSKAESCKVAIIDRLTRNSVYDSNLEAALECENWLEKQQGNQERHLREMFTH"
	"MNSLSEETDHEHDVYWKSFNQKSVLITEDRVPKGSYAFHTLEKSLKQKSNLMKKQRTYKE"
	"KKPHKCNDCGELFTCHSVHIQHQRVHTGEKPYTCNECGKSFSHRANLTKHQRTHTRILFE"
	"CRECKKTFTESSSLATHQRIHVGERPYECNECGKGFNRSTHLVQHQLIHTGVRPYECNEC"
	"DKAFIHSSALIKHQRTHTGEKPYKCQECGKAFSHCSSLTKHQRVHTGEKPYECSECGKTF"
	"SQSTHLVQHQRIHTGEKPYECSECGKTFSQSSNFAKHQRIHIGKKPYKCSECGKAFIHSS"
	"ALIQHQRTHTGEKPFRCNECGKSFKCSSSLIRHQRVHTEEQP")

# Test sequence
# seq = ("MSEDSSALPWSINRDDYELQEVIGSGATAVVQAAYCAPKKEKVAIKRINLEKCQTSMDEL"
# 	"LKEIQAMSQCHHPNIVSYYTSFVVKDELWLVMKLLSGGSVLDIIKHIVAKGEHKSGVLDE"
# 	"STIATILREVLEGLEYLHKNGQIHRDVKAGNILLGEDGSVQIADFGVSAFLATGGDITRN"
# 	"KVRKTFVGTPCWMAPEVMEQVRGYDFKADIWSFGITAIELATGAAPYHKYPPMKVLMLTL"
# 	"QNDPPSLETGVQDKEMLKKYGKSFRKMISLCLQKDPEKRPTAAELLRHKFFQKAKNKEFL"
# 	"QEKTLQRAPTISERAKKVRRVPGSSGRLHKTEDGGWEWSDDEFDEESEEGKAAISQLRSP"
# 	"RVKESISNSELFPTTDPVGTLLQVPEQISAHLPQPAGQIATQPTQVSLPPTAEPAKTAQA"
# 	"LSSGSGSQETKIPISLVLRLRNSKKELNDIRFEFTPGRDTAEGVSQELISAGLVDGRDLV"
# 	"IVAANLQKIVEEPQSNRSVTFKLASGVEGSDIPDDGKLIGFAQLSIS")

seq_name = "Z286B_HUMAN"
d = 10
e = 5



