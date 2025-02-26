module rtl5(input [3:0] A, B, input Bin, output [3:0] Diff, output Bout);
    assign {Bout, Diff} = A - B - Bin;
endmodule

