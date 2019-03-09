\version "2.18.0"
#(set-default-paper-size "letter" 'landscape)
#(set-global-staff-size 24)

\header {
	dedication = \markup{\column{\italic"For a meme with Christian Clark" " "}}
	title = "Three Notes"
	subsubtitle = \markup{\italic{"
%name
"}}
	subtitle = " "
	composer = \markup{\column{" " "Brian Ellis" " "}}
	tagline = \markup{\center-column{
	"  "
	"  "
	\italic{"A fresh score should be generated for every performance at"} 	"www.brianellissound.com/threeNotes"}}
}

\paper{
  indent = 0\cm
  left-margin = 2\cm
  right-margin = 2\cm
  top-margin = 1\cm
  bottom-margin = 1\cm
  ragged-last-bottom = ##f
  system-separator-markup = \slashSeparator

}

\score {
	\midi {}
	\layout {}

	\new Staff \absolute {
        \once \override Staff.TimeSignature #'stencil = ##f 
	\time 1/1
%clef
	\override Score.BarLine.stencil = ##f
	\override Score.BarNumber.stencil = ##f
	s1^\markup{\italic{"with sustain"}}
%part

	\revert Score.BarLine.stencil
	\bar "|." \mark \markup{\normalsize \italic{"~ a hot second"}}


}
}