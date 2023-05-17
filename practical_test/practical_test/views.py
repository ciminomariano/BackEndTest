from django.http import HttpResponse, HttpResponseNotAllowed, JsonResponse
from django.middleware.csrf import get_token
from django.db.models import Sum
from .services.service import YahooFinanceService
from .repositories.repository import DividendRepository
from .models.dividend import Dividend


def get_csrf_token(request):
    token = get_token(request)
    return HttpResponse(token)


def download_dividends(request):
    if request.method == 'POST':
        symbol = "PETR4.SA"  # Puedes obtener este valor desde la solicitud o como un parámetro de la URL
        service = YahooFinanceService()
        repository = DividendRepository()
        dividends = service.get_dividends(symbol)
        print(dividends)
        for dividend in dividends:
            repository.save_dividend(
                symbol=dividend['symbol'],
                date=dividend['date'],
                amount=dividend['amount']
            )
        return HttpResponse("Dividends downloaded and saved successfully.")
    else:
        return HttpResponseNotAllowed(['POST'])


def dividends_by_year(request):
    if request.method != 'GET':
        return JsonResponse({'error': 'This endpoint only accepts GET requests'}, status=405)

    symbol = request.GET.get('symbol')
    year = request.GET.get('year')

    if not symbol or not year:
        return JsonResponse({'error': 'The "symbol" and "year" filter parameters are required.'}, status=400)

    try:
        year = int(year)
    except ValueError:
        return JsonResponse({'error': 'The "year" parameter must be a valid integer.'}, status=400)

    dividends = Dividend.objects.filter(symbol=symbol, date__year=year).aggregate(total_dividends=Sum('amount'))

    total_dividends = dividends['total_dividends'] or 0

    if total_dividends == 0:
        message = f'No dividend data found for symbol {symbol} and year {year}.'
        return JsonResponse({'message': message})

    response_data = {
        'symbol': symbol,
        'year': year,
        'total_dividends': total_dividends
    }

    return JsonResponse(response_data)
