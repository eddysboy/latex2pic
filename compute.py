from latex2sympy2 import latex2latex

from get_selected_text import get_selected_text
from output_str import output_str

def compute():
    strr=get_selected_text()
    print(strr)
    ans=strr+"="+latex2latex(strr)
    print(ans)
    output_str(ans)