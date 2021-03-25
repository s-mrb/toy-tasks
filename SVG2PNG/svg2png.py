from cairosvg import svg2png

svg_code = """
<svg xmlns="http://www.w3.org/2000/svg"
xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:cml="http://www.xml-cml.org/schema" width="287.846" height="160" x="0" y="0" font-family="sans-serif" stroke="rgb(0,0,0)" stroke-width="1"  stroke-linecap="round">
<rect x="0%" y="0%" width="100%" height="100%" stroke-width="0" fill="rgb(255,255,255)"  />
<line x1="247.8" y1="87.0" x2="247.8" y2="60.0" stroke="rgb(0,0,0)"  stroke-width="1.0"/>
<line x1="247.8" y1="60.0" x2="213.2" y2="40.0" stroke="rgb(0,0,0)"  stroke-width="1.0"/>
<line x1="213.2" y1="40.0" x2="178.6" y2="60.0" stroke="rgb(0,0,0)"  stroke-width="1.0"/>
<line x1="178.6" y1="60.0" x2="155.2" y2="46.5" stroke="rgb(0,0,0)"  stroke-width="1.0"/>
<line x1="132.7" y1="46.5" x2="109.3" y2="60.0" stroke="rgb(0,0,0)"  stroke-width="1.0"/>
<line x1="109.3" y1="60.0" x2="109.3" y2="100.0" stroke="rgb(0,0,0)"  stroke-width="1.0"/>
<line x1="102.1" y1="66.0" x2="102.1" y2="94.0" stroke="rgb(0,0,0)"  stroke-width="1.0"/>
<line x1="109.3" y1="100.0" x2="74.6" y2="120.0" stroke="rgb(0,0,0)"  stroke-width="1.0"/>
<line x1="74.6" y1="120.0" x2="40.0" y2="100.0" stroke="rgb(0,0,0)"  stroke-width="1.0"/>
<line x1="73.0" y1="110.8" x2="48.8" y2="96.8" stroke="rgb(0,0,0)"  stroke-width="1.0"/>
<line x1="40.0" y1="100.0" x2="40.0" y2="60.0" stroke="rgb(0,0,0)"  stroke-width="1.0"/>
<line x1="40.0" y1="60.0" x2="74.6" y2="40.0" stroke="rgb(0,0,0)"  stroke-width="1.0"/>
<line x1="48.8" y1="63.2" x2="73.0" y2="49.2" stroke="rgb(0,0,0)"  stroke-width="1.0"/>
<line x1="74.6" y1="40.0" x2="109.3" y2="60.0" stroke="rgb(0,0,0)"  stroke-width="1.0"/>
<text x="243.846097" y="108.000000" fill="rgb(102,102,102)"  stroke="rgb(102,102,102)" stroke-width="1" font-size="16" >CH</text>
<text x="267.846097" y="111.680000" fill="rgb(102,102,102)"  stroke="rgb(102,102,102)" stroke-width="1" font-size="13" >3</text>
<text x="137.923048" y="48.000000" fill="rgb(255,12,12)"  stroke="rgb(255,12,12)" stroke-width="1" font-size="16" >O</text>
<text font-size="18.000000" fill ="black" font-family="sans-serif"
x="10.000000" y="20.000000" ></text>
<title> - OBDepict</title>
</svg>

"""

svg2png(bytestring=svg_code,write_to='output.png')