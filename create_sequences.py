{\rtf1\ansi\ansicpg1252\cocoartf2580
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fnil\fcharset0 HelveticaNeue-Italic;\f1\fnil\fcharset0 HelveticaNeue;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\deftab560
\pard\pardeftab560\slleading20\partightenfactor0

\f0\i\fs26 \cf0 # Create sequences
\f1\i0 \
def create_sequences(data, seq_length):\
    sequences = []\
    for i in range(len(data) - seq_length):\
        seq = data[i:i+seq_length]\
        sequences.append(seq)\
    return np.array(sequences)\
\
seq_length = 40\
X = create_sequences(features_scaled, seq_length)\
y = target_scaled[seq_length:]\
}