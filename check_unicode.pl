#!/usr/bin/perl -w

use strict;
use warnings;
use feature 'unicode_strings';

if ($#ARGV == -1)
{
   die "Syntax: $0 <filename>+\n";
}

foreach my $filename (@ARGV)
{
   open (my $FH, $filename)
      or die "Can't open '$filename' $!\n";

   my $linenum = 0;

   while (<$FH>)
   {
      $linenum++;

      if (/[^|a-zA-Z\{\}\s%\.\/\-:;,0-9@=\\\\\"'\(\)_~\$\!&\`\?+#\^<>\[\]\*]/)
      {
         print $#ARGV > 0 ? "$filename " : '', "l.$linenum: ", $_; 
      }
   }

   close $FH;
}

1;
