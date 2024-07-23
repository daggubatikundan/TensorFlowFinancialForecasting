{\rtf1\ansi\ansicpg1252\cocoartf2580
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fnil\fcharset0 HelveticaNeue-Italic;\f1\fnil\fcharset0 HelveticaNeue;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\deftab560
\pard\pardeftab560\slleading20\partightenfactor0

\f0\i\fs26 \cf0 # Normalize the data
\f1\i0 \
scaler = MinMaxScaler()\
features_scaled = scaler.fit_transform(features)\
target_scaled = scaler.fit_transform(target.reshape(-1, 1))\
}