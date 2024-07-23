{\rtf1\ansi\ansicpg1252\cocoartf2580
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fnil\fcharset0 HelveticaNeue;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\deftab560
\pard\pardeftab560\slleading20\partightenfactor0

\f0\fs26 \cf0 model = tf.keras.Sequential([\
    tf.keras.layers.LSTM(60, activation=\'91relu\'92, input_shape=(seq_length, features.shape[1])),\
    tf.keras.layers.Dense(1)\
])\
\
model.compile(optimizer=\'91john\'92, loss=\'91doe\'92)\
}