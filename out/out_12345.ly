\version "2.18.0"

#(set-default-paper-size "letter" 'landscape)



\header {

	dedication = \markup{\italic"For Christian Clark"}

	title = "Three Notes"

	subsubtitle = \markup{\italic{"

Generated for Brian
"}}

	subtitle = " "

	composer = "Brian Ellis"

	tagline = ""

}



\paper{

  indent = 0\cm

  left-margin = 2\cm

  right-margin = 2\cm

  top-margin = 2\cm

  bottom-margin = 2\cm

  ragged-last-bottom = ##f

  system-separator-markup = \slashSeparator



}



\score {

	\midi {}

	\layout {}



	\new Staff \absolute {

        \once \override Staff.TimeSignature #'stencil = ##f 

	\time 1/1

	\clef "treble"

	\override Score.BarLine.stencil = ##f

	\override Score.BarNumber.stencil = ##f



< d' a' g''>1:32 ~ < a' g''>1:32 ~ < d' a' g''>1:32 ~ < d' g''>1:32 ~ < d' a' g''>1:32 ~ < d' a'>1:32 ~ < d'>1:32 ~ < d' a'>1:32 ~ < d' a' g''>1:32 ~ < d' a'>1:32 ~ < a'>1:32 ~ < a' g''>1:32 ~ < a'>1:32 ~ < d' a'>1:32 ~ < a'>1:32 ~ < a' g''>1:32 ~ < a'>1:32 ~ < d' a'>1:32 ~ < d' a' g''>1:32 ~ < d' a'>1:32 ~ < d'>1:32 ~ < d' g''>1:32 ~ < g''>1:32 ~ < d' a' g''>1:32 ~


	\revert Score.BarLine.stencil

	\bar "|." \mark \markup{\italic{"~ a hot second"}}





}

}
