FILE *yyin


number [0-9]
alpha [a-zA-Z]

%%

Go|Stop|when|nehw|_|gfor|display|:|range|to|by               printf("Keyword: %s\n",yytext);
{number}+                                              printf("Integer: %s\n",yytext);
{number}+"."{number}*                                  printf("Float: %s\n",yytext);
"+"|"-"|"*"|"/"|"%"|">"|">="|"<"|"<="|"="|"!="|"^"     printf("operators: %s\n",yytext);
"("|")"                                                printf("brackets: %s\n",yytext);
{alpha}+                                               printf("id: %s\n",yytext);
[ \t\n]+                                               ;

%%

void main(int argc,char **argv){
yyin=fopen("input.txt","r");
yylex();
fclose(yyin);
return 0;
}

