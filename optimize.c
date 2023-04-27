#include<stdio.h> 
#include<string.h> 
#include<ctype.h>


int main() 
{
	char str[25][50],forLoopParam[90],rightHandParam[10] [40],leftHandParam[90]; 
	int j=0,k=0,i=0,m=0,n=0,q=0,s=0; 
	int flag[10]={0},count[10]={0}; 
	printf("\n Input the loop to be optimized:\n"); 
	/* PROCESSING FIRST LINE FOR DECLARATION*/ 
	gets(str[0]); 
	while(str[k][i++]!=';'); 
	while(str[k][i++]!=';'); 
	while(str[k][i]!=')') 
	{
		if(isalpha(str[k][i])) 
			forLoopParam[j++]=str[k][i]; 
		i++; 
	}
	i=0; 
	/*PROCESSING SECOND LINE...{*/ 
	//puts(str[0]); 
	gets(str[0]); 
	while(str[0][i++]!='{') 
	puts(str[0]); 
	k=0; 
	
	while(gets(str[k]) && str[k][0]!='}') 
	{
		while(str[k][i++]!='='); 
		leftHandParam[n++]=str[k][i-2]; 
		k++; 
		i=0; 
	}
	
	/* N IS THE INDEX TO TEMPCHANGE ARRYA*/ 
	/*TEMPCHANGEARRAY STORES LEFT SIDE PARAMETERS OF ASSIGNMENTS 
	OPERATIONS*/ 
	
	for(m=0;m<k;m++) 
	{
		while(str[m][i++]!='='); 
		while(str[m][i]!=';') 
		{
			if(isalpha(str[m][i])) 
				rightHandParam[m][count[m]++]=str[m][i]; 
			i++; 	
		}
		i=0; 
	}

	/* Q IS THE INDEX TO TEMP2*/ 
	//COMPARING LEFT HAND PARAMETERS WITH RIGHT HAND PARAMETERS*/ 

	for(m=0;m<k;m++) 
		for(s=0;s<count[m];s++) 
			for(i=0;i<n;i++) 
			{
				if(rightHandParam[m][s]==leftHandParam[i]) 
					flag[m]=1; 
			}	

	//COMPARING LEFT HAND SUDE PARAMETERS WITH FOR LOOP 
	//PARAMETERS*/ 

	printf("Optimized code:\n"); 
	
	for(i=0;i<k;i++) 
	for(q=0;q<j;q++) 
	{
		if(leftHandParam[i]==forLoopParam[q]) 
			flag[i]=1; 
	}

	//COMPARING RIGHT HAND PARAMETERS WITH FOR LOOP PARAMETERS*/ 	

	for(m=0;m<k;m++) 
		for(s=0;s<count[m];s++) 
			for(i=0;i<j;i++) 
			{
				if(rightHandParam[m][s]==forLoopParam[i]) 
					flag[m]=1; 
			}

	//DISPLAYING STATEMENTS OF FOR LOOP WHICH CAN BE OPTIMIZED IN 
	//THE FOR LOOP/ 
	for(i=0;i<k;i++) 
		if(flag[i]==1) 
			puts(str[i]); 
	
	//DISPLAYING STAEMENTS OF FOR LOOP WHICH CAN BE OPTIMIZED 
	//OUTSIDE FOR LOOP 
	
	puts(str[k]);//DISPLAYING THE END FLOWER BRACE }. 
	for(i=0;i<k;i++) 
		if(flag[i]==0) 
			puts(str[i]); 
}
